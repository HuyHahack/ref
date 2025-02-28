local keySystem = {
    ["huy30"] = true, -- Key hợp lệ
    ["huy30"] = true, -- Key hợp lệ
}

local function checkKey(inputKey)
    return keySystem[inputKey] or false
end

local function createUI()
    local ScreenGui = Instance.new("ScreenGui")
    local Frame = Instance.new("Frame")
    local TextBox = Instance.new("TextBox")
    local Button = Instance.new("TextButton")
    local Title = Instance.new("TextLabel")

    ScreenGui.Parent = game.CoreGui
    Frame.Parent = ScreenGui
    Frame.BackgroundColor3 = Color3.fromRGB(25, 25, 25)
    Frame.Size = UDim2.new(0, 300, 0, 200)
    Frame.Position = UDim2.new(0.5, -150, 0.5, -100)
    Frame.BorderSizePixel = 2
    Frame.BorderColor3 = Color3.fromRGB(0, 255, 127)

    Title.Parent = Frame
    Title.Text = "SCRIPT BY CGH"
    Title.Size = UDim2.new(1, 0, 0.2, 0)
    Title.TextSize = 18
    Title.TextColor3 = Color3.fromRGB(255, 255, 255)
    Title.BackgroundTransparency = 1

    TextBox.Parent = Frame
    TextBox.Size = UDim2.new(0.8, 0, 0.2, 0)
    TextBox.Position = UDim2.new(0.1, 0, 0.3, 0)
    TextBox.PlaceholderText = "Nhập key vào đây..."
    TextBox.Text = ""
    TextBox.TextSize = 16
    TextBox.BackgroundColor3 = Color3.fromRGB(40, 40, 40)
    TextBox.TextColor3 = Color3.fromRGB(255, 255, 255)

    Button.Parent = Frame
    Button.Size = UDim2.new(0.6, 0, 0.2, 0)
    Button.Position = UDim2.new(0.2, 0, 0.6, 0)
    Button.Text = "Xác nhận"
    Button.TextSize = 16
    Button.BackgroundColor3 = Color3.fromRGB(0, 200, 127)
    Button.TextColor3 = Color3.fromRGB(255, 255, 255)

    Button.MouseButton1Click:Connect(function()
        local key = TextBox.Text
        if checkKey(key) then
            ScreenGui:Destroy()
            loadstring(game:HttpGet("https://raw.githubusercontent.com/wpisstestfprg/Volcano/refs/heads/main/VolcanoNewUpdated.luau"))()
        else
            Title.Text = "Key sai! Nhập lại."
            Title.TextColor3 = Color3.fromRGB(255, 0, 0)
        end
    end)
end

createUI()
