local correctKey = "YOUR_KEY_HERE" -- Key mà mày muốn
local userInputKey

-- Hộp thoại nhập key
repeat
    userInputKey = game:GetService("Players").LocalPlayer:FindFirstChild("PlayerGui") and game:GetService("Players").LocalPlayer:FindFirstChild("PlayerGui"):FindFirstChild("ScreenGui") or Instance.new("ScreenGui", game:GetService("Players").LocalPlayer:FindFirstChild("PlayerGui"))
    local frame = Instance.new("Frame", userInputKey)
    frame.Size = UDim2.new(0, 300, 0, 150)
    frame.Position = UDim2.new(0.5, -150, 0.5, -75)
    
    local textBox = Instance.new("TextBox", frame)
    textBox.Size = UDim2.new(1, 0, 0.5, 0)
    textBox.Text = "Nhập key vào đây"

    local button = Instance.new("TextButton", frame)
    button.Size = UDim2.new(1, 0, 0.5, 0)
    button.Position = UDim2.new(0, 0, 0.5, 0)
    button.Text = "Xác nhận"
    
    button.MouseButton1Click:Connect(function()
        if textBox.Text == correctKey then
            frame:Destroy()
            print("Key chính xác! Đang tải script...")
            loadstring(game:HttpGet("https://raw.githubusercontent.com/Zunes-Bypassed/NOPE/main/Min.lua"))()
        else
            textBox.Text = "Key sai! Nhập lại!"
        end
    end)
    
    wait(10) -- Chờ 10 giây để nhập key
until false