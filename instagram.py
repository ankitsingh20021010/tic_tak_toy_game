#first step-->pip install instaloader 


import instaloader
ig = instaloader.Instaloader()
user = input("ENter user name")
ig.download_profile(user,profile_pic_only=True)
