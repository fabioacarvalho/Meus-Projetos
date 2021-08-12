<template>
    <div class="auth-content">
        <div class="auth-modal">
            <h1>NOME EMPRESA</h1>
            <div class="auth-title">
                {{ 'Login' }}
            </div>

            <input type="email" v-model="user.email" name="email" placeholder="E-mail">
            <input type="password" v-model="user.password" name="password" placeholder="Senha">
            <button @click="signin">Entrar</button>
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            user: {}
        }
    }
}
</script>

<style>
    .auth-content {
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 100px;
    }

    .auth-modal {
        background-color: #FFF;
        width: 350px;
        padding: 35px;
        box-shadow: 0 1px 5px rgba(0, 0, 0, 0.15);
        border-radius: 8px;

        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .auth-title {
        font-size: 1.2rem;
        font-weight: 100;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .auth-modal input {
        border: 1px solid #BBB;
        width: 100%;
        margin-bottom: 15px;
        padding: 3px 8px;
        outline: none;
        border-radius: 8px;
    }

    .auth-modal button {
        align-self: flex-end;
        background-color: #2460ae;
        color: #FFF;
        padding: 5px 15px;
        border-radius: 8px;
    }

    .auth-modal a {
        margin-top: 35px;
    }

    .auth-modal hr {
        border: 0;
        width: 100%;
        height: 1px;
        background-image: linear-gradient(to right,
            rgba(120, 120, 120, 0),
            rgba(120, 120, 120, 0.75),
            rgba(120, 120, 120, 0));
    }
</style>