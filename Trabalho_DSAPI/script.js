document.addEventListener('DOMContentLoaded', () => {
    const botao = document.getElementById('btn-carregar');

    botao.addEventListener('click', () => {
        fetch('clientes.xml')
            .then(response => response.text())
            .then(str => (new window.DOMParser()).parseFromString(str, "text/xml"))
            .then(data => {
                const clientes = data.getElementsByTagName('cliente');
                const lista = document.getElementById('lista-clientes');
                lista.innerHTML = '';
                for (let i = 0; i < clientes.length; i++) {
                    const id = clientes[i].getElementsByTagName('id')[0].textContent;
                    const nome = clientes[i].getElementsByTagName('nome')[0].textContent;
                    const altura = clientes[i].getElementsByTagName('altura')[0].textContent;

                    const item = document.createElement('li');
                    item.textContent = `ID: ${id}, Nome: ${nome}, Altura: ${altura}`;
                    lista.appendChild(item);
                }
            })
            .catch(err => console.error('Erro ao carregar o XML:', err));
    });
});
