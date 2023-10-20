console.log("Simulador de Memória");
console.log();
let memoria = ['0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000'];
let palavra = 4;

let menu = '';

while (menu !== 'P') {
    menu = prompt("Escolha uma Opção: \n E - Escrever \n L - Ler \n S - Status da memória \n P - Parar \n : ");
    console.log();

    if (menu === 'L') {
        let bin_endereco_leitura = prompt("Escolha um endereço: ");
        console.log();

        if (bin_endereco_leitura.length === palavra) {
            let endereco_leitura = parseInt(bin_endereco_leitura, 2);

            if (0 <= endereco_leitura <= 15) {
                console.log("Endereço " + bin_endereco_leitura + " -> " + memoria[endereco_leitura]);
                console.log();
            } else {
                console.log("Endereço inválido. Digite um endereço binário: ");
            }
        } else {
            console.log("Endereço inválido. Digite um endereço binário: ");
        }

    } else if (menu === 'E') {
        let bin_endereco_escrita = prompt("Escolha um endereço: ");

        if (bin_endereco_escrita.length === palavra) {
            let endereco_escrita = parseInt(bin_endereco_escrita, 2);

            if (0 <= endereco_escrita <= 15) {
                let valor = prompt("Digite o valor em binário a ser armazenado: ");
                console.log();

                if (valor.length === palavra) {
                    memoria[endereco_escrita] = valor;
                    console.log();
                    console.log("Valor " + valor + " armazenado no endereço " + bin_endereco_escrita + ".");
                    console.log();
                } else {
                    console.log("Valor incorreto. Digite um valor em binário: ");
                }
            } else {
                console.log("Endereço inválido. Digite um endereço binário: ");
            }
        } else {
            console.log("Endereço inválido. Digite um endereço binário: ");
        }

    } else if (menu === 'S') {
        console.log("Status da memória: ");
        for (let i = 0; i < 16; i++) {
            let endereco_binario = i.toString(2).padStart(4, '0');
            console.log(endereco_binario + " - " + memoria[i]);
        }

    } else if (menu === 'P') {
        console.log("Obrigada. Simulação Finalizada.");

    } else {
        console.log("Opção inválida. Escolha uma opção válida.");
    }
}


// variáveis do código: 

/*
valor: valor a ser armazenado

memoria: lista com índices de endereços da memória

e_endereco: endereço inserido pelo usuário em binário para operação de escrita

bin_e_endereco: endereço já transformado para binário para relacionar com o índice em "memoria" na operação de escrita

l_endereco: endereço inserido pelo usuário em binário para operação de leitura

bin_l_endereco: endereço já transformado para binário para relacionar com o índice em "memoria" na operação de leitura

menu: menu de opções
*/