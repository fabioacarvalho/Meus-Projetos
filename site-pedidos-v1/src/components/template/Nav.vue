<template>
    <!-- Cabeçalho -->
    <header id="header">
        <a id="logo" href="#">Logo</a>
        <nav id="nav">
            <!-- Menu Haburguer -->
            <button @click="toggleMenu" @touchstart="toggleMenu" id="btn-mobile" aria-label="Abril Menu" aria-haspopup="true" aria-controls="menu">Menu
                <span id="hamburguer" aria-expanded="false"></span>
            </button>
            <ul id="menu" role="menu">
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Dashboard</a></li>
                <li><a href="#">Clientes</a></li>
                <li><a href="#">Fornecedores</a></li>
                <li><a href="#">Pedidos</a></li>
                <li><a href="#">Usuarios</a></li>
                <li><a href="#">Obras</a></li>
            </ul>
        </nav>
    </header>
</template>

<script>

export default {
    /* data() {
        return {
            b: const btnMobile = document.getElementById('btn-mobile'),
            bt: btnMobile.addEventListener('click', toggleMenu),
            bt2: btnMobile.addEventListener('touchstart', toggleMenu)
        }
    }, */
    methods: {
        toggleMenu(event) {
            if(event.type === 'touchstart') event.preventDefault()
            const nav = document.getElementById('nav')
            /* toggle = Adicione caso tenha, remova caso não tenha. */
            nav.classList.toggle('active')
            const active = nav.classList.contains('active')
            event.currentTarget.setAttribute('aria-expended', active)
            if(active) {
                event.currentTarget.setAttribute('aria-label', 'Fechar menu')
            } else {
                event.currentTarget.setAttribute('aria-label', 'Abrir menu')
            }
        },
        clicarBotao() {
            this.toggleMenu()
        }       
    }
}
</script>

<style>
    /* Config Gerais */

body, ul {
    margin: 0px;
    padding: 0px;
    
}

.bgportifolio {
    background-color: rgb(209, 209, 209);
}

a {
    color: rgb(255, 255, 255);
    text-decoration: none;
    font-family: sans-serif;
}

a:hover {
    background-color: rgba(255, 255, 255, 0.05);
}

#logo {
    font-size: 1.5rem;
    font-weight: bold;
}

/* Cabeçalho Estrutura Básica */

#header {
    box-sizing: border-box;
    height: 70px;
    padding: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #3d3d3d;
}

#menu {
    display: flex;
    list-style: none;
    gap: .5rem; /* Aplica um espaçamento especifico/determinado entre os itens */
    
}

#menu a {
    display: block;
    padding: .5rem;
}

/* Esttrutura Mobile (hamburguer) */

#btn-mobile {
    display: none;
}

/* Media Q */

@media (max-width: 600px) {

    #menu {
        display: block;
        position: absolute;
        width: 100%;
        top: 70px;
        right: 0px;
        background-color: #3d3d3d;
        transition: .6s; /* Part tempo animação */
        z-index: 1000; /* Garanti que ele fique por cima */        
        height: 0px;
        visibility: hidden;
        overflow-y: hidden;

    }

    /* Animação */

    #nav.active #menu {
        height: calc(100vh - 70px);
        visibility: visible;
        overflow-y: auto;
    }

    #menu a {
        padding: 1rem 0;
        margin: 0 1rem;
        border-bottom: 2px solid rgba(0,0,0, .05);
    }

    /* Estilizando Botão */

    #btn-mobile {
        display: flex;
        padding: .5rem 1rem;
        font-size: 1rem;
        border: none;
        background: none;
        cursor: pointer;
        gap: .5rem;
        color: white;        
    }

    #hamburguer {
        border-top: 2px solid white;
        width: 20px;
    }

    /*Pseudo Elementos */

    #hamburguer::after,#hamburguer::before {
        content: '';
        display: block;
        width: 20px;
        height: 2px;
        background-color: white; /* Usa o cor do #hambuerguer */
        margin-top: 5px;
        transition: .3s;
        position: relative;
        
    }

    #nav.active #hamburguer {
        border-top-color: transparent;

    }

    #nav.active #hamburguer::before {
        transform: rotate(135deg);

    }

    #nav.active #hamburguer::after {
        transform: rotate(-135deg);
        top: -7px;

    }

}
</style>