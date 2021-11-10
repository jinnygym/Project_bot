<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Nunito&display=swap" rel="stylesheet">
	<link href="./assets/css/all.css" rel="stylesheet">
	<link href="./assets/css/fontawesome.css" rel="stylesheet">
	<title>Document</title>
	<style>
		.animation:hover {
			transform: scale(1.05, 1);
		}

		.animation {
			transition: transform 0.6s ease-out;
		}

		.animation a {
			color: #181818;
		}

		.animation a:hover {
			text-decoration: none;
			color: #181818;
		}
	</style>
	<style>
		body {
			font-family: 'Nunito', sans-serif;
		}

		.border-photo {
			border: solid 6px #594F4F;
			transition: border-width 0.6s linear;
		}

		.border-button:hover {
			border-radius: 10px;
		}

		.buttoncolor {
			color: black
		}

		.buttoncolor:hover {
			color: black
		}

		.previousPageButton {
			color: #000000;
			background-color: #ffffff;
			text-align: center;
			padding: 1%;
			font-size: 1.5vw;
			/* border-radius: 5px; */
			position: absolute;
			width: 4%;
			right: 0px;
			bottom: 55%;
			text-decoration: none;
			transition: .5s;
		}

		.previousPageButton:hover {
			text-decoration: none;
			color: #ffffff;
			background-color: #000000;
			transition: .5s;
		}

		.nextPageButton {
			color: #000000;
			background-color: #ffffff;
			text-align: center;
			padding: 1%;
			font-size: 1.5vw;
			/* border-radius: 5px; */
			width: 4%;
			position: absolute;
			right: 0;
			top: 45%;
			text-decoration: none;
			transition: .5s;
		}

		.nextPageButton:hover {
			text-decoration: none;
			color: #ffffff;
			background-color: #000000;
			transition: .5s;
		}

		.tab-next {
			width: 100%;
			height: 60px;
			margin: 10px;
			position: absolute;
			right: 0;
			top: 50%
		}
	</style>
</head>

<body style="background-color: #d4e8dc;">
	<nav class="navbar navbar-expand-lg navbar-light bg-white ">
		<a class="navbar-brand" href="https://discord.gg/bzMTBneRp5"> Dis'sabot </a>
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse">
			<a class="nav-link " href="https://github.com/jinnygym/Project_bot"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="Italian Trulli" style="width: 29px;"></a>
			<a class="nav-link " href="https://discord.com/api/oauth2/authorize?client_id=895554832725856268&permissions=17183197760&scope=bot"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqwt5C44jpf2BKbTEmZWewvlQqqN7HZeTesg&usqp=CAU" alt="Italian Trulli" style="width: 22px;"></a>
			<a class="nav-link " href="https://www.instagram.com/xviiivin/"><img src="https://www.freepnglogos.com/uploads/logo-ig-png/logo-ig-instagram-icon-download-icons-12.png" alt="Italian Trulli" style="width: 26px;">&nbsp;</a>
			<ul class="navbar-nav">
				<li class="nav-item">
					<a class="nav-link" href="https://discord.com/download">Dowload discord </a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="https://discord.com/api/oauth2/authorize?client_id=895554832725856268&permissions=17183197760&scope=bot">Add to discord</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="https://discord.gg/Yv9UBX7">Join our discord server</a><!-- รอมีอีกเว็ป -->
				</li>
			</ul>
		</div>
	</nav>
	<br>
	<br>
	<div class="container">
		<div class="row">
			<div class="col-md-2">
				<span class="badge badge-pill p-2" style="background-color:#8ad3b2; border-radius:10px">
					<h3>Dis'sabot Command</h3>
				</span>
			</div>
		</div>
		<br>
		<br>
		<!-- <div class="jumbotron jumbotron-fluid" style="background-color: #d4e8dc;"> -->
		<div class="container" style="margin-bottom: 5vh;">
			<!-- <h2 class="display-4">Command</h2>
	<ul class="list-group list-group-flush"> -->
			<li class="list-group-item animation">
				<a href="https://youtu.be/uzzHdCAbjKE">[user</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://youtu.be/yrsBZLeLZhg">[p, [play</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://www.youtube.com/watch?v=-kpGqcFfYqU">[stop</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://youtu.be/IKF0-WgDD-Y">[s, [skip</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://youtu.be/OmGtjAc5zzA">[pause</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://youtu.be/xdPwtMdSq8k">[resume</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://www.youtube.com/watch?v=ZAsuUm69V6Y">[queue, [playlist, [q</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://www.youtube.com/watch?v=j0Xakdui0P8">[dis</a>
			</li>
			<li class="list-group-item animation">
				<a href="https://youtu.be/TW2EauDK7MY">[removeSADASDAD_</a>
			</li>
			</ul>
		</div>
	</div>
	<a class="previousPageButton buttoncolor" href="/addtodiscord.php"><i class="fas fa-caret-right"></i></a>
	<a class="nextPageButton buttoncolor" href="/index.php"><i class="fas fa-caret-left"></i></a>
	<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns" crossorigin="anonymous"></script>
	<script src="assets/js/all.js"></script>
	<script src="assets/js/fontawesome.js"></script>
</body>

</html>