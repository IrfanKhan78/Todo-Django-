from django.forms import ModelForm

from .models import Todo

class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ('content', )

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['content'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Add new task'})