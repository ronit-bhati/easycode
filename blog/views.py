from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment, allIps
from django.contrib import messages
from django.db.models import Q
from blog.templatetags import extras

def blogHome(request):
    allPosts = Post.objects.all().order_by('-timeStamp')
    context = {'allPosts':allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp')
    replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('-timestamp')
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = get_client_ip(request)
    u = allIps(ips=ip, postname=post.slug)
    result = allIps.objects.filter(Q(ips__icontains=ip) and Q(postname__icontains=post.slug))
    if len(result) == 1:
        pass
    elif len(result) > 1:
        pass
    else:
        u.save()
        post.views = post.views + 1
        post.save()

    context = {'post':post, 'comments':comments, 'user':request.user, 'repDict':repDict}
    return render(request, 'blog/blogpost.html', context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")

        post = Post.objects.get(sno=postSno)

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully!")

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully!")

    return redirect(f'/blog/{post.slug}#replies')
