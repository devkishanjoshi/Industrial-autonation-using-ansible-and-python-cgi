<style>
  .speech {border: 1px solid #DDD; width: 300px; padding: 0; margin: auto; margin-top:3%;}
  .speech input {border: 0; width: 240px; display: inline-block; height: 45px;}
  .speech img {float: right; width: 40px margin: auto;}
  .menu{text-align: center; color: white; }
  body{
    margin:auto;
}
 
.bigcircle {
    margin-top:50px;
    width: 130px;
    height: 130px;
    padding: 20px;
    /*background-color: #EAEAEA;*/
    background-image: url("/var/www/html/images/moon.png");
    background-position: center;
    border-radius: 50%;
    box-shadow: 1.5px 1px 15px #000;
    margin:auto;
    text-align: center;
}
.small-circle {
    width: 70px;
    height: 70px;
    /*background-color: #c1965d;*/
    background-image: url("https://cdn3.vectorstock.com/i/1000x1000/42/12/moon-transparent-background-heavenly-body-vector-20244212.jpg");
    background-position: center;
    border-radius: 50px;
    animation-name: marire;
    animation-duration: 2s;
    animation-iteration-count: infinite; 
    margin:auto;
}

 {
    border: solid #c1965d;
    border-width: 0 10px 10px 0;
    display:inline-block;
    padding:5px;
    width:20px;
    height:20px;
    animation-name: sageata;
    animation-duration:2s;
    animation-iteration-count: infinite;
}

.down-arrow {
    transform: rotate(45deg);
    -webkit-transform: rotate(45deg);
}

@keyframes sageata {
0% {
    opacity: 0;
}
25% { 
    opacity: 0.5;
}
50% {
    opacity:1;
}
75% {
    opacity:0.5;
}
100% {
    opacity: 0;
}
}


</style>



<!-- HTML5 Speech Recognition API -->
<script>
  function startDictation() {

    if (window.hasOwnProperty('webkitSpeechRecognition')) {

      var recognition = new webkitSpeechRecognition();

      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.lang = "en-US";
      recognition.start();

      recognition.onresult = function(e) {
        document.getElementById('transcript').value
                                 = e.results[0][0].transcript;
        recognition.stop();
        document.getElementById('labnol').submit();
      };

      recognition.onerror = function(e) {
        recognition.stop();


      }

    }
  }
</script>
<body background="https://wallpapercave.com/wp/Kj5cd8B.jpg">

<div class="bigcircle">
          <div class="small-circle"></div>
          <i class="down-arrow"></i>
</div>
<!-- Search Form -->
<form id="labnol" method="get" action="http://192.168.43.252/cgi-bin/speech.py">
  <div class="speech">
    <input type="text" name="q" id="transcript" placeholder="Speak" />
    <img onclick="startDictation()" src="//i.imgur.com/cHidSVu.gif" />
  </div>
</form>
<div class="menu">
1.System Time
<br>
2.Docker
<br>
3.Send a Mail
<br>
4.Shell in a box
<br>
5.Hadoop
<br>
6.AWS Instance
<br>
7.S3 bucket(get,put,delete)
<br>
8.Yum configure
<br>
9.Service Configuration
<br>
10.IAAS (Web Server,Client)
<br>
11.Install Java 
<br>
10.Install Python
</div>
</body>
