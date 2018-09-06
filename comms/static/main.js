const commands = {

	commands: new Array(),

	execute: function(fn) {
    	this.commands.push(fn);
  	},

  	get_commands: function() {
  		try {
  			this.lock = true;

  			poll(server_host, function(resp) {
  				if (resp.body != null && resp.body.length > 0) {
  					this.execute_commands();
  				}
  			});
  		} catch(e) {
  			this.lock = false;
  			return;
  		}
  		this.lock = false;
  	}

  	execute_commands: function() {
  		if (commands.length <= 0) return;
  		this.lock = true;
  		while(commands.length > 0) {
  			let command = this.commands.pop()
  			try {
  				command();
  			} catch(e) {
  				console.error(.message)
  			}
  		}
  		this.lock = false;
  	}

};
