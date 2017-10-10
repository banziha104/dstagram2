from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Photo

@login_required
def post_list(request):
    posts = Photo.objects.all()
    return render(request,'photo/list.html',{'posts':posts})

class UploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo','text','tag']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        if form.is_valid:
            form.instance.author_id = self.request.user.id
            return redirect('/')
        else:
            return self.render_to_response({'form': form})

class PhotoDeleteV(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('post_delete')

class PhotoUpdateV(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text', 'tag']
    template_name = 'photo/upload.html'
    success_url = reverse_lazy('post_update')