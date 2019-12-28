# HV19.H01 - Hidden One

| Author | Level | Categories |
|---|---|---|
| hidden | novice | fun |

## Given
Day 06 > the Copy&Paste box contains whitespaces and tabs:

```
Born: January 22	     	 	   	   	 	       	     	  	  
Died: April 9   	  	 	    	  	      	   		  	  
Mother: Lady Anne   		 	   	   	      	  	      	  
Father: Sir Nicholas	 	      		    	    	  	  	      	      
Secrets: unknown      	 	  	 	    	    	   	       	  
```

## Approach

It's not morse, it's not ASCII, it's not a whitespace program. It's simply whitespace stego.

Credits to mcia for phrasing out what I observed, but wasn't able to type out myself - leading to the snow/stegsnow tool.
http://manpages.ubuntu.com/manpages/bionic/man1/stegsnow.1.html

```bash
# The following command probably doesn't work in a shell, but you get the point... ;)
cat << EOF
	     	 	   	   	 	       	     	  	  
   	  	 	    	  	      	   		  	  
   		 	   	   	      	  	      	  
	 	      		    	    	  	  	      	      
      	 	  	 	    	    	   	       	  
EOF > bla.txt
stegsnow -C bla.txt
```

## Flag
`HV19{1stHiddenFound}`
