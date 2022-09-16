        <div class="box side">
            <h2>Search | <a class="side" href="showall.php">Show All</a></h2>
            <hr>
            
            <i>Please use the search boxes to find sepcific reviews.</i>
            
            <hr>
                
                <!-- Start of Dish Name Search -->

                <form method="post" action="dishnamesearch.php" enctype="multipart/form-data">

                <input class="search" type="text" name='dishname' size="40" value="" required placeholder="Dish Name..."/>

                <input class="submit" type="submit" name="find_dishname" value="&#xf002"/>

                </form>

                <!-- End of Dish Name Search -->
            
            <hr>
            
                <!-- Start of Cuisine Search -->

                <form method="post" action="cuisinesearch.php" enctype="multipart/form-data">

                    <select class="cdropmenu" name="cuisine" required>

                        <option value="" disabled selected>Cuisine...</option>
                        <option value="American">American</option>
                        <option value="British">British</option>
                        <option value="French">French</option>
                        <option value="Italian">Italian</option>
                        <option value="Japanese">Japanese</option>
                        <option value="Tex-Mex">Tex-Mex</option>

                    </select>

                    <input class="submit" type="submit" name="find_cuisine" value="&#xf002"/>

                </form>

                <!-- End of Cuisine Search -->
            
            <hr>
            
                <!-- Start of Served For: Search -->

                    <form method="post" action="servedforsearch.php" enctype="multipart/form-data">

                    <select class="sdropmenu" name="servedfor" required>

                        <option value="" disabled selected>Served For:</option>
                        <option value="Breakfast">Breakfast</option>
                        <option value="Lunch">Lunch</option>
                        <option value="Dinner">Dinner</option>
                        <option value="Dessert">Dessert</option>
                        <option value="Snack">Snack</option>

                    </select>

                    <input class="submit" type="submit" name="find_servedfor" value="&#xf002"/>

                </form>

                <!-- End of Served For: Search -->
            
            <hr>
            
                <!-- Start of Rating Search -->

                <form method="post" action="ratingsearch.php" enctype="multipart/form-data">

                    <select class="halfdropmenu" name="amount">
                        <option value="exactly" selected>Exactly...</option>
                        <option value="more">At least...</option>
                        <option value="less">At most...</option>
                    </select>

                    <select class="halfdropmenu" name="stars">
                        <option value="1" selected>&#9733;</option>
                        <option value="2">&#9733;&#9733;</option>
                        <option value="3">&#9733;&#9733;&#9733;</option>
                        <option value="4">&#9733;&#9733;&#9733;&#9733;</option>
                        <option value="5">&#9733;&#9733;&#9733;&#9733;&#9733;</option>
                    </select>

                    <input class="submit" type="submit" name="find_rating" value="&#xf002"/>

                </form>

                <!-- End of Rating Search -->
            
            <hr>
            
        </div>


        <div class="box footer">
        
            <div class="license">
                
                <div class="license-image">
                <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>
                </div> <!-- / license-image -->
                
                <div class="license-text">
                This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>. &nbsp; &nbsp;
                </div> <!-- / license-text -->
            
            </div> <!-- / license -->
        
        </div> <!-- / footer -->

    </div> <!-- / wrapper -->

</body>