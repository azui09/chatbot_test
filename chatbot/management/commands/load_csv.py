import pandas as pd
from django.core.management import BaseCommand
from django.conf import settings
from chatbot.models import Produto

class Command(BaseCommand):
    help = 'Importa o novo CSV de produtos para o SQLite3'

    def handle(self, *args, **kwargs):
        caminho_arquivo = settings.BASE_DIR / 'products-10000.csv'

        try:
            df = pd.read_csv(caminho_arquivo)
            df = df.fillna('')

            df = df.drop_duplicates(subset=['Internal ID'], keep='first')

            Produto.objects.all().delete()

            produtos_para_criar = []

            for _, row in df.iterrows():
                preco_val = float(row['Price']) if row['Price'] != '' else 0.0
                estoque_val = int(row['Stock']) if row['Stock'] != '' else 0

                p = Produto(
                    internal_id=str(row['Internal ID']),
                    nome=str(row['Name']),
                    descricao=str(row['Description']),
                    marca=str(row['Brand']),
                    categoria=str(row['Category']),
                    preco=preco_val,
                    moeda=str(row['Currency']),
                    estoque=estoque_val,
                    ean=str(row['EAN']),
                    cor=str(row['Color']),
                    tamanho=str(row['Size']),
                    disponibilidade=str(row['Availability'])
                )
                produtos_para_criar.append(p)
            Produto.objects.bulk_create(produtos_para_criar, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'{len(produtos_para_criar)} produtos importados com sucesso!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Arquivo nao encontrado: {caminho_arquivo}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro fatal: {str(e)}"))