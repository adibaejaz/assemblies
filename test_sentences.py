


TEST_SENTENCES = [
    "dogs run",
    "dogs chase cats",
    "the dogs run",
    "the dogs chase cats",
    "dogs chase the cats",
    "the man saw the woman",
    "the man saw a woman",
    "the man saw a man",
    "big cats are people",
    "people are big cats",
    "the big dogs chase bad people",
    "i love you",
    "dogs run quickly",
    "the dogs run quickly",
    "the dogs quickly run",
    "dogs quickly run",
    "bad people run quickly",
    "the bad people run quickly",
    "the cats quickly chase a woman",
    "the cats quickly chase mice",
    "dogs run from cats",
    "the dogs run from cats",
    "the cats run to mice from dogs",
    "cats love the mice in people",
    "the man of the people saw the mice",
    "cats are people",
    "people are bad",  # ~Hobbes
    "big dogs are bad",
    "big bad dogs run",
    "people are big bad cats",
    "big bad cats are people",
]

RECURSIVE_TEST_SENTENCES = [
    # 1 embedding
    ("dogs chase cats who run", {0:(0,4), 1:(3,4)}),
    ("dogs chase cats who love mice", {0:(0,5), 1:(3,5)}),
    ("dogs who run fly", {0:(0,3), 1:(1,2)}),
    ("dogs who run chase cats", {0:(0,4), 1:(1,2)}),
    ("dogs who love people chase cats", {0:(0,5), 1:(1,3)}),
    ("dogs chase cats who run quickly", {0:(0,5), 1:(3,4)}),
    ("dogs chase cats who love mice quickly", {0:(0,6), 1:(3,5)}),
    ("people said dogs fly", {0:(0,3), 1:(2,3)}),
    ("people said dogs chase cats", {0:(0,4), 1:(2,4)}),
    ("people said dogs fly quickly", {0:(0,4), 1:(2,3)}),
    ("people said dogs chase cats quickly", {0:(0,5), 1:(2,4)}),
    ("the people saw the mice who fly", {0:(0,6), 1:(5,6)}),
    ("the big cats who fly quickly chase bad dogs", {0:(0,8), 1:(3,5)}),
    ("big dogs who are bad saw a bad man", {0:(0,8), 1:(2,4)}),
    # >1 level of embedding
    ("people who said dogs fly are bad", {0:(0,6), 1:(1,4), 2:(3,4)})
]