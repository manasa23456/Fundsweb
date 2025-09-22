/* General Body */
body {
    font-family: Arial, sans-serif;
    background: #f7f9fc;
    margin: 0;
    padding: 0;
    text-align: center;
    color: #111;
}

/* Container */
.container {
    width: 350px;
    margin: 50px auto;
    background: #fff;
    padding: 25px 20px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Headings */
h1 {
    margin-bottom: 20px;
    color: #0f62fe;
}
h2 {
    margin: 20px 0 10px 0;
    color: #333;
}

/* Forms */
input[type="text"],
input[type="email"],
input[type="password"],
input[type="number"] {
    width: 90%;
    padding: 10px;
    margin: 5px 0 15px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px 20px;
    background-color: #0f62fe;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s;
}

button:hover {
    background-color: #0353e9;
}

/* Links */
a {
    color: #0f62fe;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Fund List */
#fundList {
    list-style-type: none;
    padding: 0;
    margin-top: 20px;
    text-align: left;
}

#fundList li {
    background: #e3f2fd;
    margin-bottom: 8px;
    padding: 10px;
    border-radius: 6px;
}

/* Messages */
p {
    font-size: 14px;
}

p.msg {
    color: red;
    margin-bottom: 15px;
}

/* Responsive */
@media (max-width: 400px) {
    .container {
        width: 90%;
        padding: 20px;
    }
    input, button {
        width: 100%;
    }
}
