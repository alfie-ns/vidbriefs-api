
#!/bin/bash

# Get the current directory name
current_dir=$(basename "$PWD")

# Run the push script
if ./push.sh; then
  # Change to the parent directory if push.sh succeeds
  cd ..
  # Remove the original directory
  rm -rf "$current_dir"
  echo "Process completed successfully."
else
  echo "Error: push.sh failed. Exiting."
fi

# 1. Push
# 2. Back out of dir
# 3. Delete repo

# Push -> Backout -> Delete