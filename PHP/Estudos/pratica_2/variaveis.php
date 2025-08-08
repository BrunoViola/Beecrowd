<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Aula 309</title>
   </head>
   <body>
      <?php
         //string
         $nome = "Bruno";
         
         //int
         $ano = 2025;

         //float
         $peso = 60.35;

         //boolean
         $maior_idade = True;
      ?>

      <h1>Ficha Cadastral</h1>
      <hr>
      <p>
         Nome: <?php echo $nome ?>
         <br>
         Ano Cadastro: <?php echo $ano ?>
         <br>
         Peso: <?php echo $peso ?>
         <br>
         Maior de idade? <?php echo $maior_idade?>
      </p>
   </body>
</html>