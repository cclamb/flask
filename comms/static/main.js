const commands = {

  commands: new Array(),

  execute: function(fn) {
    this.commands.push(fn);
  }

};
