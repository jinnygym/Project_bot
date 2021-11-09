<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Nunito&display=swap" rel="stylesheet">
	<link href="./assets/css/all.css" rel="stylesheet">
	<link href="./assets/css/fontawesome.css" rel="stylesheet">
	<!-- <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script> -->
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

<body style="background-color: #dcd3c9 ">
	<nav class="navbar navbar-expand-lg navbar-light bg-white ">
		<a class="navbar-brand" href="https://discord.gg/bzMTBneRp5"> Dis'sabot </a>
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

		<div class="collapse navbar-collapse" id="navbarSupportedContent">
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
	<div class="container" style="margin-top:15vh;">
		<div class="row">
			<div class="col-md-3">
			</div>
			<div class="jumbotron bg-white text-black col-md-6 justify-content-center" style="border-radius: 10px;">
				<b>
					<h1 class="text-black text-center" style="font-weight: bold; ">Dis'sabot</h1>
				</b>
				<hr>
				<p>It is a bot that helps to find things on the <?php echo htmlspecialchars("<e>"); ?> ejude website and can also play music through youtube as well.</p>
				<a href="https://discord.com/api/oauth2/authorize?client_id=895554832725856268&permissions=17183197760&scope=bot"><button type="button" class="btn btn-outline-dark">Click to add bot</button></a>
			</div>
			<div class="col-md-3">
			</div>
		</div>
	</div>

	<a class="previousPageButton buttoncolor" href="/command.php"><i class="fas fa-caret-right"></i></a>
	<a class="nextPageButton buttoncolor" href="/addtodiscord.php"><i class="fas fa-caret-left"></i></a>
	<br>
	<br>
	<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns" crossorigin="anonymous"></script>
	<script src="assets/js/all.js"></script>
	<script src="assets/js/fontawesome.js"></script>
</body>
</html>