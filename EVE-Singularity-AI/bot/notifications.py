import logging
import smtplib
from email.mime.text import MIMEText
import socket
import platform

class NotificationSystem:
    def __init__(self, config):
        self.config = config
        self.last_notification = None

    def send_alert(self, message, level='info'):
        """Отправка уведомлений"""
        methods = {
            'critical': self._send_email,
            'warning': self._send_system_notification,
            'info': self._log_only
        }
        
        method = methods.get(level, self._log_only)
        method(message)

    def _send_email(self, message):
        """Отправка email через SMTP"""
        msg = MIMEText(message)
        msg['Subject'] = 'EVE Bot Alert'
        msg['From'] = self.config['email_from']
        msg['To'] = self.config['email_to']

        try:
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['smtp_user'], self.config['smtp_password'])
                server.send_message(msg)
        except Exception as e:
            self._log_only(f"Failed to send email: {str(e)}")
            
    def _log_only(self, message):
        """Просто логирование"""
        logging.info(message)