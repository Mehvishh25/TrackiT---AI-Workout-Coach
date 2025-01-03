import streamlit as st

def app():
     st.markdown("""
        <h1 style='font-size:60px;'>
            <span style='background: linear-gradient(to right, #09ebd0, #49075e);-webkit-background-clip: text;-webkit-text-fill-color: transparent;'>Explore Fitness Blogs </span>🏋‍♂
        </h1>
    """, unsafe_allow_html=True)

     st.write("""
        Discover inspiring fitness insights, tips, and resources from these amazing blogs. 
        Stay motivated and informed as you work towards your health goals.
    """)

     st.markdown(f"""
        <div style='background:linear-gradient(to right,#defcfc,#ffc7fd);border-radius: 15px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
          <h3 style='font-size: 26px; font-weight: bold; color: #0c9c95; margin-bottom: 15px;text-align:center'>Fitness Blogs 🗒</h3>
          <div style='display: flex; flex-wrap: wrap; gap: 15px;'>  <!-- Flex container for blogs -->
        <!-- First Blog -->
        <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
            <a href="https://www.health.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; background: linear-gradient(to right, #fdfbfb, #ebedee); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>Health Blog 1</a>
            <div style='font-size: 14px; color: #777; margin-top: 5px;'>- By John Doe</div>
            <div style='font-size: 14px; color: #777;'>This blog covers a wide variety of topics related to health, wellness, and fitness.</div>
        </div>   
        <!-- Second Blog -->
        <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
            <a href="https://www.fitness.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; background: linear-gradient(to right, #fdfbfb, #ebedee); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>Fitness Blog 2</a>
            <div style='font-size: 14px; color: #777; margin-top: 5px;'>- By Jane Smith</div>
            <div style='font-size: 14px; color: #777;'>A fitness blog offering expert advice on exercises and nutrition for all levels.</div>
        </div>       
        <!-- Third Blog -->
        <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
            <a href="https://www.example.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; background: linear-gradient(to right, #fdfbfb, #ebedee); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>Example Blog 3</a>
            <div style='font-size: 14px; color: #777; margin-top: 5px;'>- By Emily Johnson</div>
            <div style='font-size: 14px; color: #777;'>This blog focuses on healthy habits and fitness advice for busy people.</div>
        </div>
        <!-- Second Row (Blogs without margin-top) -->
        <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); margin-top: 0;'>
            <a href="https://www.sample.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; background: linear-gradient(to right, #fdfbfb, #ebedee); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>Sample Blog 4</a>
            <div style='font-size: 14px; color: #777; margin-top: 5px;'>- By Alex Carter</div>
            <div style='font-size: 14px; color: #777;'>A blog offering fitness tips and strategies for weight loss.</div>
        </div>       
        <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); margin-top: 0;'>
            <a href="https://www.newfitness.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; background: linear-gradient(to right, #fdfbfb, #ebedee); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>New Fitness Blog 5</a>
            <div style='font-size: 14px; color: #777; margin-top: 5px;'>- By Chris Lee</div>
            <div style='font-size: 14px; color: #777;'>A blog discussing workout routines, meal plans, and motivational advice.</div>
        </div>
     </div>
     </div>
     <div style='background-color: #ffffff; border-radius: 15px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
         <h3 style='font-size: 26px; font-weight: bold; color: #0c9c95; margin-bottom: 15px;'>Fitness Videos 🎥</h3>
         <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px;'> <!-- Grid container for videos -->
              <!-- First Video -->
              <div style='background: #f9f7fc; border-radius: 10px; padding: 10px;'>
                   <img src="https://img.youtube.com/vi/F5VWHYZnxXc/hqdefault.jpg" style="width: 100%; border-radius: 10px;" />
                   <a href="https://www.youtube.com/watch?v=F5VWHYZnxXc" target="_blank" style="font-size: 16px; font-weight: bold; color: #4f0f62; text-decoration: none;">Morning Fitness Routine</a>
                   <div style="font-size: 14px; color: #777;">500K views</div>
              </div>
              <!-- Second Video -->
              <div style='background: #f9f7fc; border-radius: 10px; padding: 10px;'>
                   <img src="https://img.youtube.com/vi/ihba9Lw0tv4/hqdefault.jpg" style="width: 100%; border-radius: 10px;" />
                   <a href="https://www.youtube.com/watch?v=ihba9Lw0tv4" target="_blank" style="font-size: 16px; font-weight: bold; color: #4f0f62; text-decoration: none;">Cardio Tips for Beginners</a>
                   <div style="font-size: 14px; color: #777;">350K views</div>
              </div>
              <!-- Third Video -->
              <div style='background: #f9f7fc; border-radius: 10px; padding: 10px;'>
                   <img src="https://img.youtube.com/vi/2euHNg3twUU/hqdefault.jpg" style="width: 100%; border-radius: 10px;" />
                   <a href="https://www.youtube.com/watch?v=2euHNg3twUU" target="_blank" style="font-size: 16px; font-weight: bold; color: #4f0f62; text-decoration: none;">HIIT Training Guide</a>
                   <div style="font-size: 14px; color: #777;">1.2M views</div>
              </div>
              <!-- Add more videos as needed -->
         </div>
    </div>
    <div style="margin-top:50px; padding:2px; border-radius:10px; max-width:1200px; margin-left:auto; margin-right:auto; background:#ffffff;">
        <h2 style="margin:10px; text-align:center; margin-bottom:25px;">
            <span style="color:#0c9c95;">Healthy Meals</span> 🍽
        </h2>
        <div style="
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 15px; 
            justify-content: center;">
            <!-- Video 1 -->
            <div style="border-radius:10px; padding:10px; background: linear-gradient(to bottom, #f9f7fc, #e3d7fc);">
                <img src="https://img.youtube.com/vi/F6ehz4iK3F8/hqdefault.jpg" 
                    style="width: 100%; border-radius:10px; margin-bottom:10px;" />
                <a href="https://www.youtube.com/watch?v=F6ehz4iK3F8" 
                    target="_blank" 
                    style="font-size:18px; font-weight:bold; color:#4f0f62; text-decoration:none;">Healthy Meal Prep Ideas 1</a>
                <div style="font-size:14px; color:#777;">120K views</div>
            </div>
            <!-- Video 2 -->
            <div style="border-radius:10px; padding:10px; background: linear-gradient(to bottom, #f9f7fc, #e3d7fc);">
                <img src="https://img.youtube.com/vi/5-tU58d13q0/hqdefault.jpg" 
                    style="width: 100%; border-radius:10px; margin-bottom:10px;" />
                <a href="https://www.youtube.com/watch?v=5-tU58d13q0" 
                    target="_blank" 
                    style="font-size:18px; font-weight:bold; color:#4f0f62; text-decoration:none;">Healthy Meal Prep Ideas 2</a>
                <div style="font-size:14px; color:#777;">95K views</div>
            </div>
            <!-- Video 3 -->
            <div style="border-radius:10px; padding:10px; background: linear-gradient(to bottom, #f9f7fc, #e3d7fc);">
                <img src="https://img.youtube.com/vi/U5GP-o6K3IQ/hqdefault.jpg" 
                    style="width: 100%; border-radius:10px; margin-bottom:10px;" />
                <a href="https://www.youtube.com/watch?v=U5GP-o6K3IQ" 
                    target="_blank" 
                    style="font-size:18px; font-weight:bold; color:#4f0f62; text-decoration:none;">Healthy Meal Prep Ideas 3</a>
                <div style="font-size:14px; color:#777;">150K views</div>
            </div>
            <!-- Video 4 -->
            <div style="border-radius:10px; padding:10px; background: linear-gradient(to bottom, #f9f7fc, #e3d7fc);">
                <img src="https://img.youtube.com/vi/z9KClaGjo9A/hqdefault.jpg" 
                    style="width: 100%; border-radius:10px; margin-bottom:10px;" />
                <a href="https://www.youtube.com/watch?v=z9KClaGjo9A" 
                    target="_blank" 
                    style="font-size:18px; font-weight:bold; color:#4f0f62; text-decoration:none;">Healthy Meal Prep Ideas 4</a>
                <div style="font-size:14px; color:#777;">105K views</div>
            </div>
            <!-- Video 5 -->
            <div style="border-radius:10px; padding:10px; background: linear-gradient(to bottom, #f9f7fc, #e3d7fc);">
                <img src="https://img.youtube.com/vi/j4iQkKYFH1E/hqdefault.jpg" 
                    style="width: 100%; border-radius:10px; margin-bottom:10px;" />
                <a href="https://www.youtube.com/watch?v=j4iQkKYFH1E" 
                    target="_blank" 
                    style="font-size:18px; font-weight:bold; color:#4f0f62; text-decoration:none;">Healthy Meal Prep Ideas 5</a>
                <div style="font-size:14px; color:#777;">85K views</div>
            </div>
        </div>
    </div>


    """, unsafe_allow_html=True)