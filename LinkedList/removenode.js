class LinkedListNode {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }

  function  deleteNode(b){
  
    const nextnode = b.next;
    if(nextnode.value){
        b.value = nextnode.value;
        b.next = nextnode.next;
      
    }
    else(
      console.log('cant delete node which is the last one with this technique')
    )
   
} 
  
  const a = new LinkedListNode('A');
  const b = new LinkedListNode('B');
  const c = new LinkedListNode('C');
  
  a.next = b;
  b.next = c;
  
 deleteNode(b);
