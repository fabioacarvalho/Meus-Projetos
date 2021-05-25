<template>
    <div class="general container-fluid">

        <nav class="navbar navbar-expand-lg navbar-light float-end">
            <div class="container-fluid justify-content-end">
                <span class="navbar-toggler ">Contato</span>
                <button class="navbar-toggler " type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    
                    <span class="navbar-toggler-icon"></span>
                    
                </button>
                
                <div class="collapse navbar-collapse " id="navbarSupportedContent">
                    <ul class="navbar-nav float-end  ">
                        <li class="nav-item ">
                            <a class="p-2 bd-highlight" target="_blank" href="https://github.com/fabioacarvalho">
                                <img class="img-fluid " id="linkgituhub" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" data-canonical-src="https://img.shields.io/badge/github-%23100000.svg?&amp;style=for-the-badge&amp;logo=github&amp;logoColor=white&amp;link=mailto:https://github.com/fabioacarvalho">
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="p-2 bd-highlight" target="_blank" href="mailto:fabio22191@gmail.com">
                                <img class="img-fluid" id="linkgmail" src="https://www.vectorlogo.zone/logos/gmail/gmail-tile.svg" data-canonical-src="https://img.shields.io/badge/gmail-D14836?&amp;style=for-the-badge&amp;logo=gmail&amp;logoColor=white&amp;link=mailto:fabio22191@gmail.com">
                            </a>   
                        </li>
                        <li class="nav-item">
                            <a class="p-2 bd-highlight" target="_blank" href="https://www.linkedin.com/in/fabio-carvalho-881026142/" rel="nofollow">
                                <img class="img-fluid" id="linklinkedin" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-tile.svg" data-canonical-src="https://img.shields.io/badge/linkedin-%230077B5.svg?&amp;style=for-the-badge&amp;logo=linkedin&amp;logoColor=white&amp;link=mailto:https://www.linkedin.com/in/fabio-carvalho-881026142/">
                            </a>
                        </li>
                        
                        
                    </ul>
                </div>
            </div>
        </nav>      


        <div class="container-fluid justify-content-center">
            <div class="row row-cols-1">
                <div class="col-1"><h1 class="text-xl-start white text-wrap" id="nome">FÁBIO CARVALHO</h1>
                    <div class="col-2"><h1 class="h2 text-xl-start white" id="portifolio">PORTIFÓLIO</h1></div>
                
                </div>
                <div class="col-10"><img id="fotofabio" class="img-fluid mx-auto d-bloc" width="75%" src="../assets/imagens/fabio-perfil.png" alt="Perfil"></div>
            </div>
        </div>


            
        <div class="container-fluid d-flex">
            
            
        </div>
        
        
    </div>
</template>

<script>

export default {
    
}
</script>

<style>



    div, .general {
        background-image: url("../assets/imagens/capa.png");
        background-repeat: no-repeat;
    }
    
    #portifolio {
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }

    #nome, #sobrenome {
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        
    }

    #linklinkedin {
        width: 50px;
    }

    #linkgmail {
        width: 50px;
    }

    #linkgituhub {
        width: 50px;
    }

    

</style>