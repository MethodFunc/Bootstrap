from Project import app, load_movie_lr, load_movie_nb, load_iris, load_indians, tw_tokenizer

load_movie_lr()
load_movie_nb()
load_iris()
load_indians()
app.run(host='0.0.0.0')       # 외부 접속 허용시 app.run(host='0.0.0.0')