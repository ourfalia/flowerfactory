# from django.shortcuts import render
# from django.core.mail import send_mail, BadHeaderError
# from .models import Contact
# from .forms import ContactForm

# from django.shortcuts import render, redirect, reverse
# from django.contrib import messages
# from .models import Post, Comment
# from .forms import CommentForm
# import warnings


# # Create your views here.


# def send_email(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#     else:
#         form = ContactForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'contact/contact.html', context)

# def post_details(request, id):
#     post_details = Post.objects.get(id=id)
#     comments = Comment.objects.filter(post=post_details)

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if not request.user.is_authenticated:
#             messages.error(request, 'Sorry, You need to log in to comment.')
#             return redirect(reverse('post_details', args=[id]))

#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.user = request.user
#             new_comment.post = post_details
#             new_comment.save()

#             return redirect(reverse('post_details', args=[id]))
#     else:
#         comment_form = CommentForm()

#     context = {
#         'post_details': post_details,
#         'comments': comments,
#         'comment_form': comment_form,
#     }

#     return render(request, 'blog/post_details.html', context)