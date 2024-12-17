import fire

from src import body_content, body_title, mime_text, sender, subject_title


def send_mail(project_name, log_file):
    subject_ = subject_title(project_name)
    body_title_ = body_title()
    body_content_ = body_content(log_file)
    body_ = mime_text(body_title_, body_content_)

    sender(subject_, body_)


if __name__ == '__main__':
    fire.Fire(send_mail)
