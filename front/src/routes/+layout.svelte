<script>
    let { children } = $props();
</script>

<style>
    nav {
        background-color: #FADADD; /* Rosa pastel claro */
        padding: 1rem;
        display: flex;
        justify-content: center;
        gap: 1rem;
        border-radius: 10px; /* Borda arredondada */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */
    }

    nav a {
        color: #B56576; /* Rosa pastel mais escuro */
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2rem;
        transition: color 0.3s, transform 0.3s; /* Animações suaves */
    }

    nav a:hover {
        color: #6D597A; /* Tom roxo pastel */
        transform: scale(1.1); /* Amplia levemente ao passar o mouse */
    }

    nav a:active {
        color: #355070; /* Azul pastel escuro */
    }

    main {
        padding: 2rem;
        background-color: #FFE5EC; /* Fundo leve para o conteúdo */
        border-radius: 10px;
        margin: 1rem;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Sombra para o conteúdo */
    }
</style>

<nav>
    <a href="/">home</a>
    <a href="/movies">filmes</a>
    <a href="/artists">artistas</a>
</nav>

<main>
    {@render children()}
</main>
