import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import os
from datetime import datetime

email_user = ''
email_password = ''
log_file = 'email_log.csv'

def send_email(to_emails, subject, message):
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(email_user, email_password)

        for to_email in to_emails:
            try:
                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                smtp_server.sendmail(email_user, to_email, msg.as_string())

                log_email(to_email, subject, message)

                print(f"E-mail enviado com sucesso para {to_email}!")
            except Exception as e:
                print(f"Erro ao enviar e-mail para {to_email}: {e}")

        smtp_server.quit()
    except Exception as e:
        print(f"Erro ao conectar ao servidor SMTP: {e}")

def log_email(to_email, subject, message):
    file_exists = os.path.isfile(log_file)
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Data/Hora', 'Destinatário', 'Assunto', 'Mensagem'])
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([current_time, to_email, subject, message])

def show_email_log():
    if not os.path.isfile(log_file):
        print("Nenhum e-mail foi enviado ainda.")
        return

    with open(log_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                print(f"Data/Hora: {row[0]}, Destinarário: {row[1]}, Assunto: {row[2]}, Mensagem: {row[3]}")
            else:
                print(f"Linha inválida encontrada: {row}")

def main():
    while True:
        print(" ███╗   ███╗███████╗███╗   ██╗██╗   ██╗  ")
        print(" ████╗ ████║██╔════╝████╗  ██║██║   ██║  ")
        print(" ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║  ")
        print(" ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║  ")
        print(" ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝  ")
        print(" ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   ")
        print("Create By : Theuseng")
        print()
        print("           [1]> Enviar E-mail")
        print("           [2]> Ver Histórico de E-mails")
        print()
        print(" [0]> Exit")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            to_emails = input("Digite os e-mails dos destinatários (separados por vírgula): ").split(',')
            to_emails = [email.strip() for email in to_emails]
            subject = input("Digite o assunto do e-mail: ")
            message = input("Digite a mensagem do e-mail: ")
            send_email(to_emails, subject, message)
        elif choice == '2':
            show_email_log()
        elif choice == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor escolha novamente.")

if __name__ == "__main__":
    main()
