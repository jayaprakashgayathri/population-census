<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Login - Population Census</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-image: url('enhanced_image.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }

        .login-container {
            width: 350px;
            margin: 80px auto;
            background: #23383f;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
            text-align: center;
        }

        h2 {
            color: #81c784;
            margin-bottom: 20px;
        }

        input {
            width: 85%;
            padding: 12px;
            margin: 12px 0;
            border: none;
            border-radius: 6px;
            font-size: 14px;
        }

        input:focus {
            outline: none;
            box-shadow: 0 0 5px #81c784;
        }

        button {
            width: 90%;
            padding: 12px;
            background: #81c784;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.3s;
        }

        button:hover {
            background: #66bb6a;
        }

        .home-button {
            display: inline-block;
            margin-bottom: 20px;
            padding: 8px 16px;
            background: #81c784;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
            transition: 0.3s;
        }

        .home-button:hover {
            background: #66bb6a;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <a href="homepage.html" class="home-button">Home</a>
        <h2>Login</h2>
        <input type="text" id="username" placeholder="Username">
        <input type="password" id="password" placeholder="Password">
        <button onclick="login()">Login</button>
    </div>

    <script>
        function login() {
            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;
            if (username === 'user123' && password === 'population') {
                alert('Login successful!');
                window.location.href = 'homepage.html';
            } else {
                alert('Invalid username or password!');
            }
        }
    </script>
</body>
</html>
