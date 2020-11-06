import os
from ftplib import FTP

# Config
ftpEndereco ='endereço do ftp' 
usuarioLogin = 'nome do usuário do ftp'
usuarioSenha = 'senha de acesso ao ftp'
ftpPastaOrigem = "subpasta do ftp"
usuarioPastaDestino = r"C:\Users\Dev\Desktop\ftpDownload"

# Acesso
ftp = FTP(ftpEndereco)
ftp.login(usuarioLogin,usuarioSenha)

ftp.cwd(ftpPastaOrigem) # seleção da pasta no FTP
os.chdir(usuarioPastaDestino) # seleção da pasta para onde devem ir os arquivos baixados
arquivoFTP = ftp.nlst() #lista os arquivos do FTP
qtdArquivos = str(len(arquivoFTP))
print("Total de Arquivos para download: " + qtdArquivos)

contador = 0
for	nomeArquivo in arquivoFTP:
	contador += 1
	arquivoLocal = open(nomeArquivo, 'wb')
	print(str(contador) + " de " + qtdArquivos + ". baixando: "+ nomeArquivo)
	ftp.retrbinary('RETR ' + nomeArquivo, arquivoLocal.write)
	arquivoLocal.close()
ftp.quit()