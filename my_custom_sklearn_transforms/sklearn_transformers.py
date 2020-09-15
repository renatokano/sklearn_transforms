from sklearn.base import BaseEstimator, TransformerMixin
# Preprocessing for IBM Challenge 2 - 2020
class PreProcessingColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data['REPROVACAO_HUMANAS'] = ((data['REPROVACOES_DE']+data['REPROVACOES_EM']) > 0)
        data['REPROVACAO_EXATAS'] = ((data['REPROVACOES_MF']+data['REPROVACOES_GO']) > 0).astype(int)
        data['MEDIA_HUMANAS'] = ((data['NOTA_DE']+data['NOTA_EM'])/2).astype(float)
        data['MEDIA_EXATAS'] = ((data['NOTA_MF']+data['NOTA_GO'])/2).astype(float)
        data['MEDIA_GERAL'] = ((data['NOTA_MF']+data['NOTA_GO']+data['NOTA_DE']+data['NOTA_EM'])/4).astype(float)

        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')