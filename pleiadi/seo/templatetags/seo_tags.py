def show_seo(seo_model):
    choices = poll.choice_set.all()
    return {'choices': choices}