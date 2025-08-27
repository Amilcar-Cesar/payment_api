import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(sef):
        #criar id de pagamento da instituição financeira
        bank_payment_id = str(uuid.uuid4())

        #copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'
        
        #QR code
        img = qrcode.make(hash_payment)
        
        #salva imagem como arquivo PNG
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {"bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"}
        