from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import Tweet, Hashtag, Follow
from django.contrib.auth.models import User


def profile_view(request, author):
    current_user = User.objects.get(username=author)
    name = current_user.first_name + " " + current_user.last_name
    tweets = Tweet.objects.filter(author=current_user).order_by('-date')
    following = Follow.objects.filter(following_user=current_user)
    followers = Follow.objects.filter(user=current_user)

    return render(request, "profile.html",
                  {"author": author,
                   "name": name,
                   "tweets": tweets,
                   "user": request.user,
                   "followings": following,
                   "followers": followers
                   })


def follow_view(request, author):
    user = User.objects.get(username=author)
    following_user = User.objects.get(username=request.user.username)

    if user != following_user and not Follow.objects.filter(user=user, following_user=following_user).exists():
        Follow.objects.create(user=user, following_user=following_user)

    return redirect('/profile/' + author)


def unfollow_view(request, author):
    user = User.objects.get(username=author)
    following_user = User.objects.get(username=request.user.username)

    if user != following_user and Follow.objects.filter(user=user, following_user=following_user).exists():
        Follow.objects.filter(user=user, following_user=following_user).delete()

    return redirect('/profile/' + author)


def like_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])

    if tweet.likes.filter(pk=request.user.pk).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)

    return redirect('/')


def hashtag_view(request):
    hashtag = Hashtag.objects.get(id=request.GET['id'])
    tweets = Tweet.objects.filter(hashtag=hashtag).order_by('-date')
    return render(request, "hashtag.html", {"hashtag": hashtag, "tweets": tweets})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render('accounts/error=True')


def signup_view(request):
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )

    login(request, user)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


def accounts_view(request):
    return render(request, 'accounts.html', {})


def delete_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    tweet.delete()
    return redirect('/')


def main_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts')

    if request.method == 'POST':
        tweet = Tweet(
            body=request.POST['body'],
            author=request.user
        )
        tweet.save()

        tokens = request.POST['body'].split(' ')
        for token in tokens:
            if token[0] == "#" and len(token) > 0:
                if Hashtag.objects.filter(hashtag=token[1:]).exists():
                    hashtag = Hashtag.objects.get(hashtag=token[1:])
                    hashtag.tweets.add(tweet)
                else:
                    hashtag = Hashtag(hashtag=token[1:])
                    hashtag.save()
                    hashtag.tweets.add(tweet)

    tweets = Tweet.objects.order_by('-date')
    hashtags = Hashtag.objects.all()
    user = User.objects.get(username=request.user)
    name = user.first_name + " " + user.last_name
    return render(request, 'main.html', {'tweets': tweets, 'user': request.user, 'name': name, 'hashtags': hashtags})
