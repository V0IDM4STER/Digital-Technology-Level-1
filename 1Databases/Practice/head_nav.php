<!DOCTYPE html>

<html lang="en">
    
<?php
  
    session_start();
    include("config.php");
    include("functions.php"); // Include database sanitisation
        
    // Connect to database...
        
    $dbconnect=mysqli_connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);
    
    if (mysqli_connect_errno())
        
    {
        echo "Connection failed:".mysqli_connect_errno(); exit;
    }
    
?>

<head>
    <meta charset="UTF-8">
    <meta name="description" content= "Book Fan Reading Reviews">
    <meta name="keywords" content= "books, reading, review">
    <meta name="author" content= "Daniel Hesp">
    <meta name="viewport" content= "width=device-width, initial-scale=1.0">

    <title>Book Fan Reading Reviews</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Gideon+Roman&family=Libre+Baskerville&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link rel="stylesheet" href="bookstyle.css">

</head>
    
<body>
    
    <div class="wrapper">
        
        <a href="index.php" title="Home">
            <div class="box logo">
            </div> <!-- / logo -->
        </a>
        <div class="box banner">
        <h1>Book Fan Reading Reviews</h1>
        </div> <!-- / banner -->

        <div class="box nav">
        <a href="index.php">Home</a> |
        <a href="contact.php">Contact</a>
        </div> <!-- / nav -->