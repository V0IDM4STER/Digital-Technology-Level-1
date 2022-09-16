<div class="box side">
        
            <h3>Search | <a class="side" href="showall.php">Show All</a></h3>
            
            <i>Type part of title / author name and then search</i>
            
            <hr />
            
            <!-- Start of Title Search -->
    
            <form method="post" action="titlesearch.php" enctype="multipart/form-data">
                
                <input class="search" type="text" name='title' size="40" value="" required placeholder="Title..."/>
                
                <input class="submit" type="submit" name="find_title" value="Search"/>
    
            </form>
    
            <!-- End of Title Search -->
    
            <!-- Start of Author Search -->
    
            <form method="post" action="authorsearch.php" enctype="multipart/form-data">
                
                <input class="search" type="text" name='author' size="40" value="" required placeholder="Author..."/>
                
                <input class="submit" type="submit" name="find_author" value="Search"/>
    
            </form>
    
            <!-- End of Author Search -->
    
            <hr />
    
                <i>Use the dropdown menus below to search by genre or rating.</i>
    
            <hr />
    
            <!-- Start of Genre Search -->
    
            <form method="post" action="genresearch.php" enctype="multipart/form-data">
                
                <select name="genre" required>
                
                    <option value="" disabled selected>Genre...</option>
                    <option value="Historical Fiction">Historical Fiction</option>
                    <option value="Humour">Humour</option>
                    <option value="Non Fiction">Non Fiction</option>
                    <option value="Sci Fi">Science Fiction</option>
                    <option value="Thriller">Thriller</option>

                </select>
                
                <input class="submit" type="submit" name="find_genre" value="Search"/>
    
            </form>
    
            <!-- End of Genre Search -->

            <!-- Start of Rating Search -->
    
            <form method="post" action="ratingsearch.php" enctype="multipart/form-data">
                
                <select class="half_width" name="amount">
                    <option value="exactly">Exactly...</option>
                    <option value="more" selected>At least...</option>
                    <option value="less">At most...</option>
                </select>
    
                <select class="half_width" name="stars">
                    <option value="1">&#9733;</option>
                    <option value="2">&#9733;&#9733;</option>
                    <option value="3" selected>&#9733;&#9733;&#9733;</option>
                    <option value="4">&#9733;&#9733;&#9733;&#9733;</option>
                    <option value="5">&#9733;&#9733;&#9733;&#9733;&#9733;</option>
                </select>
                
                <input class="submit" type="submit" name="find_rating" value="Search"/>
            
            </form>
    
            
    
            <!-- Start of Rating Search -->

            <hr ?>
            
    </div> <!-- /side -->

        <div class="box footer">
        CC DEH 2022
        </div> <!-- / footer -->

</div> <!-- / wrapper -->

</body>