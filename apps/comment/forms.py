from django import forms


class CommentForm(forms.Form):
	content_type 	= forms.CharField(widget=forms.HiddenInput)
	object_id 		= forms.CharField(widget=forms.HiddenInput)
	# parent_id		= forms.CharField(widget=forms.HiddenInput,required=False)# @use -> reply
	content 		= forms.CharField(widget=forms.Textarea(),label="")

