import markovify

def langdon_generator(tweets):
    # build model
    text_model = markovify.NewlineText(tweets)

    # make a new genre:
    tweet = text_model.make_short_sentence(280)
    if '@' in tweet:
        langdon_generator(tweets)
    print(f'markov - langdon brand bullshit: {tweet}')
    return tweet