# Python OTP Verification System using SMTP

Overview
This Python OTP (One-Time Password) Verification System is a simple yet effective way to implement two-factor authentication (2FA) in your applications. By utilizing the Simple Mail Transfer Protocol (SMTP), this system sends a unique one-time password to the user's email address, ensuring secure access to their accounts.

Features
Secure Authentication: Enhance the security of your application by implementing two-factor authentication.
Customizable OTP Generation: Generate OTPs of variable length and complexity to suit your security needs.
Email Integration: Utilize SMTP to seamlessly send OTPs to users' email addresses.
Configurable Settings: Easily configure SMTP server details and email templates to fit your application's requirements.
Error Handling: Implement robust error handling to manage exceptions and ensure system reliability.

Screenshots
![default](https://github.com/RahulMirashi/OTP-verification-system-with-Python/assets/67996693/54beecfe-67f0-4935-90d9-927e1ef62e0f)

The exception is thrown when the entered email is invalid.
![Invalid email](https://github.com/RahulMirashi/OTP-verification-system-with-Python/assets/67996693/7629f2ad-b9d4-4df4-9c73-cc441fc88a2b)

OTP generated on entered valid email address.
![Email OTP](https://github.com/RahulMirashi/OTP-verification-system-with-Python/assets/67996693/636c338f-814d-4a45-a493-01f98677db30)

The exception is thrown when the entered OTP is incorrect.
![Incorrect OTP](https://github.com/RahulMirashi/OTP-verification-system-with-Python/assets/67996693/19ce544e-a9dd-4559-84c8-ebb87ae431ad)

The exception is thrown when the entered OTP is invalid (OTP length not equal to 6).
![Invalid OTP](https://github.com/RahulMirashi/OTP-verification-system-with-Python/assets/67996693/1468d751-5eba-43ec-8b94-16d583627915)

The validation is thrown when the entered OTP is valid.
![Valid OTP](https://github.com/RahulMirashi/OTP-verification-system-with-Python/assets/67996693/0550eafc-509a-462f-9aef-883d02a7e99e)

