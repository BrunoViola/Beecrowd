<?php
    $valor1 = readline();
    $valor2 = readline();
    
    $media = ($valor1*3.5 + $valor2*7.5) /11;
    
    echo "MEDIA = ".number_format($media,5,".","")."\n";
?>