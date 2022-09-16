<?php include("head-nav.php"); 

$showall_sql="SELECT * FROM `food_reviews` WHERE `Served For:` LIKE '%dinner%' ORDER BY `food_reviews`.`Dish Name` ASC";
$showall_query=mysqli_query($dbconnect, $showall_sql);
$showall_rs=mysqli_fetch_assoc($showall_query);
$count=mysqli_num_rows($showall_query);

?>

    <div class="box main">
        
        <div class="box text">
            
            <h2>Dinner Reviews</h2>
            
            <?php
            
            // Check if there are any results
            
            if ($count<1)
                
            {
                
            ?>
            
            <div class="error">
                Sorry! There are no results that match your search. Please use the search box in the sidebar to try again.
            </div>
            
            <?php
            
            } // end count 'if'
            
            // If there are not results, output an error
            
            else {
                
                do {
                    
                ?>
                
                <!-- Results go here -->
            
                <hr>

                    <p>Dish Name: <span class="sub-heading"><?php echo $showall_rs['Dish Name']; ?></span></p>

                    <p>Cuisine: <span class="sub-heading"><?php echo $showall_rs['Cuisine']; ?></span></p>

                    <p>Served For: <span class="sub-heading"><?php echo $showall_rs['Served For:']; ?></span></p>

                    <p>Rating: <span class="sub-heading">
                        
                        <?php 
                        
                            for ($x=0; $x < $showall_rs['Rating']; $x++)
                                
                            {
                               echo "&#9733;"; 
                            }
                        
                            // Generate stars until it matches the Rating number
                    
                        ?>
                        
                        </span></p>

                    <p><span class="sub-heading">Review / Response</span></p>

                    <p>
                        <?php echo $showall_rs['Review']; ?>
                    </p>
            
                <hr>
            
                <br />
            
                <?php
                    
                } // end do
                
                while($showall_rs=mysqli_fetch_assoc($showall_query));
                
            } // end else
            
            // If there are results, display them
            
            ?>
        
        </div> <!-- / text -->
    
    </div> <!-- / main -->

<?php include("sidefooter.php"); ?>