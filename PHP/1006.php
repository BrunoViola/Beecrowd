<?php
    $valor1 = readline();
    $valor2 = readline();
    $valor3 = readline();
    
    $media = ($valor1*2 + $valor2*3 + $valor3*5) /10;
    
    echo "MEDIA = ".number_format($media,1,".","")."\n";
?>