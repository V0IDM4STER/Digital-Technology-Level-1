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
    <meta name="description" content= "Daniel's Food Reviews">
    <meta name="keywords" content= "food, review, nachos, lasagne, fish and chips">
    <meta name="author" content= "Daniel Hesp">
    <meta name="viewport" content= "width=device-width, initial-scale=1.0">
    
    <title>Daniel's Food Reviews</title>
    
    <link rel="stylesheet" href="CSS/font-awesome.min.css">
    <link rel="stylesheet" href="CSS/foodstyle.css">
    
    <link href="https://fonts.googleapis.com/css2?family=Cabin&family=Lobster&display=swap" rel="stylesheet">
    
</head>
    
<body>
    
    <div class="wrapper">
    
        <a href="index.php" title="Home">
        <div class="box logo">
        </div> <!-- / logo -->
        </a>
        
        <div class="box banner">
            <h1>Daniel's Food Reviews</h1>        
        </div> <!-- / banner -->
        
        <div class="box nav">
            <a href="index.php">Home</a> |
            <a href="breakfast.php">Breakfast</a> |
            <a href="lunch.php">Lunch</a> |
            <a href="dinner.php">Dinner</a> |
            <a href="contact.php">Contact</a>
        </div> <!-- / nav -->