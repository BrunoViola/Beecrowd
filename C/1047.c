#include <stdio.h>

int main()
{
    int horarioInicio, horarioFim, minutoInicio, minutoFim;
    int horasDecorridas, minutosDecorridos, duracaoPartida;
    
    scanf("%d %d %d %d", &horarioInicio, &minutoInicio, &horarioFim, &minutoFim);
    
    int tempoInicio = horarioInicio*60 + minutoInicio; //calculando a quantidade de minutos 
    int tempoFim = horarioFim*60 + minutoFim; //calulando a quantidade de minutos
    
    if (tempoInicio < tempoFim){ //se o jogo começou e terminou no mesmo dia
        duracaoPartida = tempoFim - tempoInicio; //calculo os minutos que a partida durou
        if(duracaoPartida>=60){ //se a partida passou de 60 minutos, devo calcular a quantidade de horas
            horasDecorridas = duracaoPartida/60; //cálculo das horas decorridas
            duracaoPartida -= horasDecorridas*60; //retiro o valor dos minutos que formam horas inteiras
            minutosDecorridos = duracaoPartida;
        }
        else{//se a partida durou menos que 60 minutos, atribuo apenas a quantidade de minutosDecorridos
            horasDecorridas = 0;
            minutosDecorridos = duracaoPartida;
        }
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horasDecorridas, minutosDecorridos);
    
    }else if(tempoInicio == tempoFim){ //se o jogo teve duração máxima de 24 horas
        horasDecorridas = 24;
        minutosDecorridos = 0;
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horasDecorridas, minutosDecorridos);
    
    }else{ //se o jogo começou em um dia e terminou no dia seguinte
        int quantidadeMinutosDia = 24*60; //quantidade de minutos em um dia
        duracaoPartida = tempoFim-tempoInicio; //o resultado será negativo, mas somando com a quantidade de minutos por dia, consigo obter a duração em minutos da partida
        duracaoPartida += quantidadeMinutosDia;

        if(duracaoPartida>=60){ //se a partida passou de 60 minutos, devo calcular a quantidade de horas
            horasDecorridas = duracaoPartida/60; //cálculo das horas decorridas
            duracaoPartida -= horasDecorridas*60; //retiro o valor dos minutos que formam horas inteiras
            minutosDecorridos = duracaoPartida;
        }

        else{ //se a partida durou menos que 60 minutos, atribuo apenas a quantidade de minutosDecorridos
            horasDecorridas = 0;
            minutosDecorridos = duracaoPartida;
        }
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horasDecorridas, minutosDecorridos);
    }

    return 0;
}
