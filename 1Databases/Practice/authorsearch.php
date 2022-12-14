<?php include("head_nav.php"); 

if (isset($_POST['find_author']))
    
{

// Retrieves author and sanitises it
$author=test_input(mysqli_real_escape_string($dbconnect, $_POST['author']));
    
$showall_sql="SELECT * FROM `book_reviews` WHERE `Author` LIKE '%$author%' ORDER BY `Author` ASC";
$showall_query=mysqli_query($dbconnect, $showall_sql);
$showall_rs=mysqli_fetch_assoc($showall_query);
$count=mysqli_num_rows($showall_query);

?>
        
        <div class="box main">
            
            <h2>Author Search</h2>
            
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
            
                    <div class="results">

                    <p>Title: <span class="sub_heading"><?php echo $showall_rs['Title']; ?></span></p>

                    <p>Author: <span class="sub_heading"><?php echo $showall_rs['Author']; ?></span></p>

                    <p>Genre (Text Type): <span class="sub_heading"><?php echo $showall_rs['Genre']; ?></span></p>

                    <p>Rating: <span class="sub_heading">
                        
                        <?php 
                        
                            for ($x=0; $x < $showall_rs['Rating']; $x++)
                                
                            {
                               echo "&#9733;"; 
                            }
                        
                        ?>
                        
                        </span></p>

                    <p><span class="sub_heading">Review / Response</span></p>

                    <p>
                        <?php echo $showall_rs['Review']; ?>
                    </p>

                    </div> <!-- end results -->
            
                <br />
            
                <?php
                    
                } // end do
                
                while($showall_rs=mysqli_fetch_assoc($showall_query));
                
            } // end else
    
            } // end isset
            
            // If there are results, display them
            
            ?>
        
        </div> <!-- / main -->

<?php include("sidefoot.php"); ?>