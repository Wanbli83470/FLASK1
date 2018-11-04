from flask import abort

class Post():

	POSTS = [
		{'id' : '1', 'title' : 'Tibet', 'content': "Pays d'origine"},
		{'id' : '2', 'title' : 'Lhassa', 'content': "Ville d'origine"},
		{'id' : '3', 'title' : 'surnom', 'content': "Lion des neiges"},
		{'id' : '4', 'title' : 'Poil', 'content': "Soyeux"},
	]

	@classmethod
	def all(cls):
		return cls.POSTS

	@classmethod
	def find(cls, id):
		try :
			return cls.POSTS[int(id) - 1]
		except IndexError:
			abort(404)
