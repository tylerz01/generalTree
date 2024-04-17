document.addEventListener('DOMContentLoaded', () => {
    const nodes = document.querySelectorAll('.node, .child-node');
    
    nodes.forEach(node => {
        node.addEventListener('click', (e) => {
            e.stopPropagation(); 
            nodes.forEach(n => n.classList.remove('highlight')); 
            node.classList.add('highlight'); 
        });
    });
});