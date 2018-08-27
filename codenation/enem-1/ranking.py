import pandas as pd


def ranking():
    train = pd.read_csv("train.csv")

    df_answer = pd.DataFrame()
    df_answer['NU_INSCRICAO'] = train['NU_INSCRICAO']
    df_answer['NOTA_FINAL'] = ((train['NU_NOTA_CN'] * 2) + train['NU_NOTA_CH'] + (train['NU_NOTA_LC'] * 1.5) + (train['NU_NOTA_MT'] * 3) + (train['NU_NOTA_REDACAO'] * 3)) / 10.5

    df_ranking = df_answer.sort_values('NOTA_FINAL', ascending=False).head(20)
    df_ranking.to_csv("answer.csv", index=False)

if __name__ == '__main__':
    ranking()
