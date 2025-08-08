<?php
   //verifica se a autenticacao foi realizada
   $usuario_autenticado = false;

   $usuarios_app = array(
      array('email'=>'adm@teste.br', 'senha'=>'1234'),
      array('email'=>'user@teste.br', 'senha'=>'4321'),
   );
   foreach($usuarios_app as $user) {
      print('Usuário: '.$user['email']);
      echo '<br>';
      print('Senha: '.$user['senha']);
      echo '<hr>';

      if($user['email'] == $_POST['email'] && $user['senha'] == $_POST['senha']){
         $usuario_autenticado = true;
      }
   }

   if($usuario_autenticado){
      echo 'Usuário autenticado';
   }else{
      header('Location: index.php?login=erro');
   }
?>